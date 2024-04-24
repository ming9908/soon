package controller

import (
	"fmt"
	"main/src/service"
	"strings"
)

type HTTPController struct {
	svc  *service.SoonService
	sKey string
}

func NewHTTPController(svc *service.SoonService, key string) *HTTPController {
	return &HTTPController{
		svc:  svc,
		sKey: key,
	}
}

type response struct {
	Success bool        `json:"success"`
	Message string      `json:"message"`
	Data    interface{} `json:"data"`
}

func GetResponse() *response {
	return &response{}
}

func responseSetSuccess(r *response) {
	r.Success = true
}

func responseSetBindError(r *response) {
	r.Message = "request data struct is wrong"
}

func responseSetMissingData(r *response, data ...string) {
	msData := []string{}
	for _, str := range data {
		msData = append(msData, str)
	}

	r.Message = fmt.Sprintf("data is missing. check data <%s>", strings.Join(msData, ","))
}

func responseSetWrongData(r *response, data ...string) {
	wData := []string{}
	for _, str := range data {
		wData = append(wData, str)
	}

	r.Message = fmt.Sprintf("data is wrong. check data <%s>", strings.Join(wData, ","))
}

func responseSetUnauthorized(r *response, data ...string) {
	wData := []string{}
	for _, str := range data {
		wData = append(wData, str)
	}

	r.Message = "unauthorized"
}
