package controller

import (
	"main/src/auth"
	"main/src/service"
	"net/http"

	"github.com/gin-gonic/gin"
)

func (h *HTTPController) PostUser(ctx *gin.Context) {
	rsp := &response{}
	req := service.UserReq{}

	err := ctx.Bind(&req)
	if err != nil {
		responseSetBindError(rsp)
		ctx.JSON(http.StatusBadRequest, rsp)
		return
	}

	// data valid check
	if req.UserID == "" || req.Password == "" || req.Nick == "" || req.PrivacyPolicy == "" {
		responseSetMissingData(rsp, "phone", "password", "nick", "privacy_policy")
		ctx.JSON(http.StatusBadRequest, rsp)
		return
	}

	// insert user
	err = h.svc.MakeUser(req)
	if err != nil {
		rsp.Message = err.Error()
		ctx.JSON(http.StatusFailedDependency, rsp)
		return
	}

	responseSetSuccess(rsp)
	ctx.JSON(http.StatusOK, rsp)
}

func (h *HTTPController) LoginUser(ctx *gin.Context) {
	rsp := &response{}
	req := service.UserReq{}

	err := ctx.Bind(&req)
	if err != nil {
		responseSetBindError(rsp)
		ctx.JSON(http.StatusBadRequest, rsp)
		return
	}

	// user check
	user, err := h.svc.LoginUserCheck(req)
	if err != nil {
		rsp.Message = "휴대전화번호 또는 비밀번호가 틀렸습니다."
		ctx.JSON(http.StatusUnauthorized, rsp)
		return
	}

	//token 발급
	accessToken, err := auth.MakeJWTToken(user.UserID, h.sKey)
	if err != nil {
		rsp.Message = "로그인 실패"
		ctx.JSON(http.StatusUnauthorized, rsp)
		return
	}
	rsp.Data = auth.RspToken{
		AccessToken: accessToken,
	}

	responseSetSuccess(rsp)
	ctx.JSON(http.StatusOK, rsp)
}

func (h *HTTPController) GetUser(ctx *gin.Context) {
	rsp := &response{}

	user_id := ctx.GetString("user_id")

	user, err := h.svc.GetUser(user_id)
	if err != nil {
		rsp.Message = err.Error()
		ctx.JSON(http.StatusFailedDependency, rsp)
		return
	}

	rsp.Data = user
	responseSetSuccess(rsp)
	ctx.JSON(http.StatusOK, rsp)
}

func (h *HTTPController) DeleteUser(ctx *gin.Context) {
	rsp := &response{}

	user_id := ctx.GetString("user_id")

	err := h.svc.DeleteUser(user_id)
	if err != nil {
		rsp.Message = err.Error()
		ctx.JSON(http.StatusFailedDependency, rsp)
		return
	}

	responseSetSuccess(rsp)
	ctx.JSON(http.StatusOK, rsp)
}
