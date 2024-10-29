import 'package:flutter/material.dart';
import 'package:soon_front/common/common.dart';


class Soon extends StatelessWidget {
  const Soon({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SOON Demo',
      theme: ThemeData(
        /** 컬러스키마를 설정하면 입력한 색상 위주로 기본적인 세팅이 이루어진다고 합니다. */
        colorScheme: ColorScheme.fromSeed(seedColor: soon),
        useMaterial3: true,
      ),
      home: const SoonMainPage(title: 'SOON'),
    );
  }
}

class SoonMainPage extends StatefulWidget {
  const SoonMainPage({super.key, required this.title});

  final String title;

  @override
  State<SoonMainPage> createState() => _SoonMainPageState();
}

class _SoonMainPageState extends State<SoonMainPage> {
  @override
  // 화면을 그리는 메인 함수 느낌쓰
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
        elevation: 0,
        centerTitle: false,
        /** leading => 타이틀 텍스트 왼쪽 정렬(주로 햄버거 버튼) */
        // leading: const IconButton(onPressed: null, icon: Icon(Icons.menu)),
        /** actions => 타이틀 텍스트 오른쪽 정렬(위젯 배열 사용 가능) */
        actions: const [
          IconButton(onPressed: null, icon: Icon(
            Icons.notifications,
              color: warn,
              size: 30,
            ),
          )
          
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: 
            <Widget>[
              Card(
                color: const Color(0xffF9D2D2),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: <Widget>[
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: <Widget>[
                        TextButton(
                          child: const Text('BUY TICKETS'),
                          onPressed: () {/* ... */},
                        ),
                        const SizedBox(width: 8),
                        TextButton(
                          child: const Text('LISTEN'),
                          onPressed: () {/* ... */},
                        ),
                        const SizedBox(width: 8),
                      ],
                    ),
                  ],
                ),
              ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: null,
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
      ),
    );
  }
}
