package repository

import (
	"fmt"
	"time"
)

type User struct {
	Id            int
	UserID        string
	Password      string
	Nick          string
	PrivatePolicy string
	CreateAt      string
	Stat          string
}

func (m *MysqlRepository) InsertUser(u *User) error {
	_, err := m.db.Exec("insert into user(user_id, password, nickname, private_policy) values (?, password(?), ?, ?)", u.UserID, u.Password, u.Nick, u.PrivatePolicy)
	return err
}

func (m *MysqlRepository) CheckUserID(userID string) (bool, error) {
	count := 0
	duple := false

	err := m.db.QueryRow("select count(*) from user where user_id = ? and stat = 'A'", userID).Scan(&count)
	if err != nil {
		fmt.Printf("db Exec error : %s", err.Error())
	}

	if count > 0 {
		duple = true
	}
	return duple, err
}

func (m *MysqlRepository) SelectUserForLogin(user *User) (User, error) {
	u := User{}

	err := m.db.QueryRow("select user_id, nick, private_policy, create_at from user where user_id = ? and password = password(?) and stat = 'A'",
		user.UserID, user.Password).Scan(&u.UserID, &u.Nick, &u.PrivatePolicy, &u.CreateAt)

	return u, err
}

func (m *MysqlRepository) SelectUser(userID string) (User, error) {
	u := User{}

	err := m.db.QueryRow("select user_id, nick, private_policy, create_at from user where user_id = ? and stat = 'A'",
		userID).Scan(&u.UserID, &u.Nick, &u.PrivatePolicy, &u.CreateAt)

	return u, err
}

func (m *MysqlRepository) DeleteUser(userID string) error {
	del_date := fmt.Sprintf("D-%s", time.Now().Format("2006-01-02 15:04:05"))
	_, err := m.db.Exec("update user set stat=? where user_id = ?", del_date, userID)
	return err
}
