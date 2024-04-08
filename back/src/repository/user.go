package repository

import "fmt"

type User struct {
	Id       int
	Phone    string
	Password string
	Stat     string
}

func (m *MysqlRepository) InsertUser(u *User) error {
	_, err := m.db.Exec("insert into user(phone, password) values (?, password(?))", u.Phone, u.Password)
	return err
}

/*
	ChechUser
	> 기존에 있는 사용자인지 확인합니다.

	return
	true : 기존에 가입한 적이 있는 사용자인 경우
	false : 기존에 존재하지 않는 사용자일 경우
*/
func (m *MysqlRepository) CheckUserPhone(phone string) (bool, error) {
	count := 0
	duple := false

	err := m.db.QueryRow("select count(*) from user where phone = ? and stat = 'A'", phone).Scan(&count)
	if err != nil {
		fmt.Printf("db Exec error : %s", err.Error())
	}

	if count > 0 {
		duple = true
	}
	return duple, err
}

func (m *MysqlRepository) SelectUser(user *User) (User, error) {
	u := User{}

	err := m.db.QueryRow("select id, phone from user where phone = ? and password = password(?) and stat = 'A'", user.Phone, user.Password).Scan(&u.Id, &u.Phone)

	return u, err
}

func (m *MysqlRepository) SelectUserByPhone(phone string) (bool, error) {
	count := 0
	err := m.db.QueryRow("select count(*) from user where phone = ? and stat = 'A'", phone).Scan(&count)
	if err != nil {
		return false, err
	}
	if count < 1 {
		return false, err
	}

	return true, err
}
