import 'package:flutter/material.dart';
import 'package:soon_front/common/common.dart';

class SoonFab extends StatefulWidget {
  const SoonFab({super.key});
  
  @override
  State<SoonFab> createState() => _SoonFabState();
}

class _SoonFabState extends State<SoonFab>
    with SingleTickerProviderStateMixin {
  /** FloatingActionButton */
  bool isOpened = false;
  late AnimationController _animationController;
  // late Animation<Color> _buttonColor;
  // late Animation<double> _animateIcon;
  late Animation<double> _translateButton;
  final Curve _curve = Curves.easeOut;
  final double _fabHeight = 56.0;

  @override
  initState() {
    _animationController =
        AnimationController(vsync: this, duration: const Duration(milliseconds: 500))
          ..addListener(() {
            setState(() {});
          });
    // _animateIcon =
    //     Tween<double>(begin: 0.0, end: 1.0).animate(_animationController);
    // _buttonColor = ColorTween(
    //   begin: Colors.blue,
    //   end: Colors.red,
    // ).animate(CurvedAnimation(
    //   parent: _animationController,
    //   curve: Interval(
    //     0.00,
    //     1.00,
    //     curve: Curves.linear,
    //   ),
    // ));
    _translateButton = Tween<double>(
      begin: _fabHeight,
      end: -14.0,
    ).animate(CurvedAnimation(
      parent: _animationController,
      curve: Interval(
        0.0,
        0.75,
        curve: _curve,
      ),
    ));
    super.initState();
  }

  @override
  dispose() {
    _animationController.dispose();
    super.dispose();
  }

  animate() {
    if (!isOpened) {
      _animationController.forward();
    } else {
      _animationController.reverse();
    }
    isOpened = !isOpened;
  }

  Widget add() {
    return FloatingActionButton(
      onPressed: null,
      tooltip: 'Add',
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(50),
      ),
      child: const Icon(Icons.add),
    );
  }

  Widget image() {
    return FloatingActionButton(
      onPressed: null,
      tooltip: 'Image',
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(50),
      ),
      child: const Icon(Icons.image),
    );
  }

  Widget inbox() {
    return FloatingActionButton(
      onPressed: null,
      tooltip: 'Inbox',
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(50),
      ),
      child: const Icon(Icons.inbox),
    );
  }

  Widget toggle() {
    return FloatingActionButton(
      backgroundColor: soon,
      onPressed: animate,
      tooltip: '순 빠른 실행',
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(50),
      ),
      child: Image.asset(
        '$IMAGE_SRC/plant_white.png',
        width: 40,
        height: 40,
      ),
      // child: AnimatedIcon(
      //   icon: AnimatedIcons.menu_close,
      //   progress: _animateIcon,
      // ),
    );
    /**
    FloatingActionButton(
      onPressed: setMenuShow,
      tooltip: '플로팅버튼',  // 오래 클릭하면 뜨는 툴팁 문구 설정
      backgroundColor: transparency,
      shape: RoundedRectangleBorder(
        // 모서리 라운드
        borderRadius: BorderRadius.circular(50),
      ),
      // elevation은 그림자 효과
      elevation: 0,
      hoverElevation: 0,
      focusElevation: 0,
      highlightElevation: 0,
      child: Image.asset('$IMAGE_SRC/soon.png')
      // child: const SvgIcon(name: 'soon'),
    )
    */
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.end,
      children: <Widget>[
        Transform(
          transform: Matrix4.translationValues(
            0.0,
            _translateButton.value * 3.0,
            0.0,
          ),
          child: add(),
        ),
        Transform(
          transform: Matrix4.translationValues(
            0.0,
            _translateButton.value * 2.0,
            0.0,
          ),
          child: image(),
        ),
        Transform(
          transform: Matrix4.translationValues(
            0.0,
            _translateButton.value,
            0.0,
          ),
          child: inbox(),
        ),
        toggle(),
      ],
    );
  }
}
