import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

const String DEFAULT_ASSET_SRC = 'assets';
const String IMAGE_SRC = '$DEFAULT_ASSET_SRC/image';
const String ICON_SRC = '$DEFAULT_ASSET_SRC/icon';
const String FONT_SRC = '$DEFAULT_ASSET_SRC/font';

// 아이콘 스타일
class SvgIcon extends StatelessWidget {
  final String name;

  const SvgIcon(String s, {
    super.key, 
    required this.name,
  });

  @override
  Widget build(BuildContext context) {
    return SvgPicture.asset(
      '$ICON_SRC/$name.svg',
    );
  }
}

Widget soonSvgIcon () {
  return (
    SvgPicture.asset(
      '$ICON_SRC/soon.svg',
    )
  );
}

Widget svgIcon (name) {
  return (
    SvgPicture.asset(
      '$ICON_SRC/$name.svg',
    )
  );
}

/**
 * svg 파일 사용
 * 
 * 1. 파일 상단에 import 'package:flutter_svg/flutter_svg.dart'; 모듈 선언
 * 2. SvgPicture.asset({...}) => 어플리케이션 자체 파일 경로(/assets/...)
 *    SvgPicture.network({...}) => 외부 파일 경로
 *    파일 경로 필수 / 사이즈 선택
 * 
 *  - SvgIcon => 파일명만 입력하면 svg 파일을 위젯으로 반환해 줌
 */