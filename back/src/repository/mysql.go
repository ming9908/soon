package repository

import (
	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

type MysqlRepository struct {
	db *sql.DB
}

func NewMysqlRepository() *MysqlRepository {
	db, err := sql.Open("mysql", "root:1234@tcp(s_mysql:3306)/soon")
	if err != nil {
		panic(err)
	}

	return &MysqlRepository{
		db: db,
	}
}
