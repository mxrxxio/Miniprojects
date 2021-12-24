package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"
)

type Album struct {
	Feed struct {
		Title  string `json:"title"`
		ID     string `json:"id"`
		Author struct {
			Name string `json:"name"`
			URL  string `json:"url"`
		} `json:"author"`
		Links []struct {
			Self string `json:"self"`
		} `json:"links"`
		Copyright string `json:"copyright"`
		Country   string `json:"country"`
		Icon      string `json:"icon"`
		Updated   string `json:"updated"`
		Results   []struct {
			ArtistName            string `json:"artistName"`
			ID                    string `json:"id"`
			Name                  string `json:"name"`
			ReleaseDate           string `json:"releaseDate"`
			Kind                  string `json:"kind"`
			ArtistID              string `json:"artistId"`
			ArtistURL             string `json:"artistUrl"`
			ContentAdvisoryRating string `json:"contentAdvisoryRating,omitempty"`
			ArtworkURL100         string `json:"artworkUrl100"`
			Genres                []struct {
				GenreID string `json:"genreId"`
				Name    string `json:"name"`
				URL     string `json:"url"`
			} `json:"genres"`
			URL string `json:"url"`
		} `json:"results"`
	} `json:"feed"`
}

var client *http.Client

func getAlbum() {
	url := "https://rss.applemarketingtools.com/api/v2/us/music/most-played/10/albums.json"
	var newAlbum Album
	err := getJson(url, &newAlbum)
	if err != nil {
		log.Fatal(err.Error())
	} else {
		// fmt.Printf("That album: %T\n ", newAlbum.Feed.Results)
		for i := 1; i <= len(newAlbum.Feed.Results); i++ {
			fmt.Printf("%d Artist: %v \n Title: %v\n", i, newAlbum.Feed.Results[i-1].ArtistName, newAlbum.Feed.Results[i-1].Name)
		}
	}
}

func getJson(url string, target interface{}) error {
	resp, err := client.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	return json.NewDecoder(resp.Body).Decode(target)
}

func main() {
	fmt.Println("Testing...")
	client = &http.Client{Timeout: 10 * time.Second}
	getAlbum()
}
