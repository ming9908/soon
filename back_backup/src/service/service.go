package service

import (
	"main/src/repository"
	"strings"

	"github.com/google/uuid"
)

type SoonService struct {
	mysql *repository.MysqlRepository
}

func NewService(mysql *repository.MysqlRepository) *SoonService {
	return &SoonService{
		mysql: mysql,
	}
}

func newUUID() string {
	return strings.Replace(uuid.New().String(), "-", "", -1)
}
