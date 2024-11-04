package service

import (
	"fmt"
	"main/src/repository"
)

type UserReq struct {
	UserID        string `json:"user_id"`
	Password      string `json:"password"`
	Nick          string `json:"nickname"`
	PrivacyPolicy string `json:"privacy_policy"`
}

type UserRsp struct {
	UserID        string `json:"user_id"`
	Nick          string `json:"nickname"`
	PrivacyPolicy string `json:"privacy_policy"`
	CreateAt      string `json:"create_at"`
}

func (s *SoonService) MakeUser(u UserReq) error {

	// check duplicate
	dupl, err := s.mysql.CheckUserID(u.UserID)
	if err != nil {
		return err
	} else if dupl {
		return fmt.Errorf("이미 존재하는 아이디입니다.")
	}

	user := &repository.User{
		UserID:        u.UserID,
		Password:      u.Password,
		Nick:          u.Nick,
		PrivatePolicy: u.PrivacyPolicy,
	}

	// user insert
	err = s.mysql.InsertUser(user)
	if err != nil {
		return fmt.Errorf("사용자 등록에 실패했습니다.")
	}

	return err
}

func (s *SoonService) LoginUserCheck(u UserReq) (repository.User, error) {
	var err error
	userData := repository.User{}

	// select user
	user := &repository.User{
		UserID:   u.UserID,
		Password: u.Password,
	}

	userData, err = s.mysql.SelectUserForLogin(user)
	return userData, err
}

func (s *SoonService) GetUser(userID string) (UserRsp, error) {

	user, err := s.mysql.SelectUser(userID)
	if err != nil {
		return UserRsp{}, err
	}

	return UserRsp{
		UserID:        user.UserID,
		Nick:          user.Nick,
		PrivacyPolicy: user.PrivatePolicy,
		CreateAt:      user.CreateAt,
	}, nil
}

func (s *SoonService) DeleteUser(userID string) error {
	return s.mysql.DeleteUser(userID)
}
