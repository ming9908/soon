package main

import (
	"main/src/auth"
	"main/src/controller"
	"main/src/repository"
	"main/src/service"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func main() {
	mysqlRepo := repository.NewMysqlRepository()
	svc := service.NewService(mysqlRepo)

	router := gin.Default()
	// httpCon := controller.NewHTTPController(svc, os.Getenv("SECRET_KEY"))

	//route
	router.GET("/api/soon/status", func(ctx *gin.Context) { ctx.String(http.StatusOK, "ready\n") })
	//User
	// router.POST("/api/soon/users", httpCon.PostUser)
	// router.POST("/api/soon/users/login", httpCon.LoginUser)

	//check auth
	router.Use(AuthMiddleware(svc))

	router.Run(":8080")
}

func AuthMiddleware(svc *service.SoonService) gin.HandlerFunc {
	return func(c *gin.Context) {
		rsp := controller.GetResponse()
		token := c.GetHeader("Authorization")
		userPhone, err := auth.ValidateToken(token, os.Getenv("SECRET_KEY"))
		if err != nil {
			rsp.Meta.Code = http.StatusUnauthorized
			rsp.Meta.Message = "unauthorized"
			c.JSON(http.StatusUnauthorized, rsp)
			c.Abort()
			return
		}
		c.Set("phone", userPhone)
		c.Next()
	}
}
