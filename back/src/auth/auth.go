package auth

import (
	"time"

	_ "github.com/dgrijalva/jwt-go"
	"github.com/dgrijalva/jwt-go/v4"
)

type AuthClaims struct {
	Phone string `json:"phone"`
	jwt.StandardClaims
}

type RspToken struct {
	AccessToken string `json:"access_token"`
}

func MakeJWTToken(phone, secretKey string) (string, error) {
	at := AuthClaims{
		Phone: phone,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: jwt.At(time.Now().Add(time.Minute * 60)),
		},
	}

	atoken := jwt.NewWithClaims(jwt.SigningMethodHS256, &at)
	token, err := atoken.SignedString([]byte(secretKey))

	if err != nil {
		return token, err
	}

	return token, err
}

func ValidateToken(token, secretKey string) (string, error) {
	claim := &AuthClaims{}
	_, err := jwt.ParseWithClaims(token, claim, func(token *jwt.Token) (interface{}, error) {
		return []byte(secretKey), nil
	})
	if err != nil {
		return claim.Phone, err
	}

	return claim.Phone, err
}
