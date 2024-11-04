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
	httpCon := controller.NewHTTPController(svc, os.Getenv("SECRET_KEY"))

	//route
	router.GET("/api/soon/status", func(ctx *gin.Context) { ctx.String(http.StatusOK, "ready\n") })
	//User
	router.POST("/api/soon/user", httpCon.PostUser)
	router.POST("/api/soon/login", httpCon.LoginUser)

	//check auth
	router.Use(AuthMiddleware(svc))

	//User
	router.GET("/api/soon/user", httpCon.GetUser)
	router.DELETE("/api/soon/user", httpCon.DeleteUser)

	router.Run(":8080")
}

func AuthMiddleware(svc *service.SoonService) gin.HandlerFunc {
	return func(c *gin.Context) {
		rsp := controller.GetResponse()
		token := c.GetHeader("Authorization")
		user_id, err := auth.ValidateToken(token, os.Getenv("SECRET_KEY"))
		if err != nil {
			rsp.Message = "unauthorized"
			c.JSON(http.StatusUnauthorized, rsp)
			c.Abort()
			return
		}
		c.Set("user_id", user_id)
		c.Next()
	}
}
