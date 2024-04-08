package controller

import (
	"fmt"
	"main/src/service"
	"net/http"
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
	Meta struct {
		Code    int    `json:"code"`
		Message string `json:"message"`
	} `json:"meta"`
	Data interface{} `json:"data"`
}

func GetResponse() *response {
	return &response{}
}

func responseSetSuccess(r *response) {
	r.Meta.Code = http.StatusOK
	r.Meta.Message = "ok"
}

func responseSetBindError(r *response) {
	r.Meta.Code = http.StatusBadRequest
	r.Meta.Message = "request data struct is wrong"
}

func responseSetMissingData(r *response, data ...string) {
	msData := []string{}
	for _, str := range data {
		msData = append(msData, str)
	}

	r.Meta.Code = http.StatusBadRequest
	r.Meta.Message = fmt.Sprintf("data is missing. check data <%s>", strings.Join(msData, ","))
}

func responseSetWrongData(r *response, data ...string) {
	wData := []string{}
	for _, str := range data {
		wData = append(wData, str)
	}

	r.Meta.Code = http.StatusBadRequest
	r.Meta.Message = fmt.Sprintf("data is wrong. check data <%s>", strings.Join(wData, ","))
}

func responseSetUnauthorized(r *response, data ...string) {
	wData := []string{}
	for _, str := range data {
		wData = append(wData, str)
	}

	r.Meta.Code = http.StatusUnauthorized
	r.Meta.Message = "unauthorized"
}
