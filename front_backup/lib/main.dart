import 'package:flutter/material.dart';
import 'package:soon_front/common/common.dart';
import 'package:soon_front/common/widget/main/week_calendar.dart';
import 'package:soon_front/common/widget/soon_fab.dart';

void main() {
  /** 메인 함수
   *  Soon이라는 클래스를 가동시키며 앱을 가동한다는 뜻
   * */
  runApp(const Soon());
  /**
   * StatelessWidget(SLW)
   *  - 상태변화 없
   * StatefulWidget(SFW)
   *  - 상태변화 있
   *  - react useState와 유사
   *  - setState로 상태 변화 관리
   *  - flutter는 setState로 함수가 실행되면 build 메서드 재호출
   */

  /**
   * Flutter run key commands.
   * r Hot reload. 🔥🔥🔥
   * R Hot restart.
   * h List all available interactive commands.
   * d Detach (terminate "flutter run" but leave application running).
   * c Clear the screen
   * q Quit (terminate the application on the device).
   */
}

class Soon extends StatelessWidget {
  const Soon({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SOON Demo',
      theme: ThemeData(
        // This is the theme of your application.
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a purple toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.

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

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<SoonMainPage> createState() => _SoonMainPageState();
}

class _SoonMainPageState extends State<SoonMainPage> {
  @override
  Widget build(BuildContext context) {
    /** 화면을 그리는 메인 함수 느낌쓰 */
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // TRY THIS: Try changing the color here to a specific color (to
        // Colors.amber, perhaps?) and trigger a hot reload to see the AppBar
        // change color while the other colors stay the same.
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        // Here we take the value from the SoonMainPage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
        elevation: 0,
        centerTitle: false,
        toolbarHeight: 40,
        /** leading => 타이틀 텍스트 왼쪽 정렬(주로 햄버거 버튼) */
        // leading: const IconButton(
        //   onPressed: null
        //   , icon: Icon(Icons.arrow_back
        //   , color: black
        // )),
        /** actions => 타이틀 텍스트 오른쪽 정렬(위젯 배열 사용 가능) */
        actions: const [
          IconButton(onPressed: null, icon: Icon(
            Icons.notifications,
              // Icons.notifications_active,
              color: warn,
              size: 30,
            ),
          )
        ],
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        // constraints: const BoxConstraints.expand(), // Container
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          //
          // TRY THIS: Invoke "debug painting" (choose the "Toggle Debug Paint"
          // action in the IDE, or press "p" in the console), to see the
          // wireframe for each widget.
          mainAxisAlignment: MainAxisAlignment.start,
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
              Card(
                color: Colors.white,
                child: weekCalendar(),
              ),

              /*
              Card(
                color: Colors.white,
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: const <Widget>[
                     ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    const ListTile(
                      leading: Icon(Icons.album),
                      title: Text('The Enchanted Nightingale'),
                      subtitle: Text('Music by Julie Gable. Lyrics by Sidney Stein.'),
                    ),
                    // Row(
                    //   mainAxisAlignment: MainAxisAlignment.end,
                    //   children: <Widget>[
                    //     TextButton(
                    //       child: const Text('BUY TICKETS'),
                    //       onPressed: () {/* ... */},
                    //     ),
                    //     const SizedBox(width: 8),
                    //     TextButton(
                    //       child: const Text('LISTEN'),
                    //       onPressed: () {/* ... */},
                    //     ),
                    //     const SizedBox(width: 8),
                    //   ],
                    // ),
                  ],
                ),
              ),*/
          ],
        ),
      ),
    floatingActionButton: const SoonFab(),
      // This trailing comma makes auto-formatting nicer for build  methods.
    );
  }
}


// The overflowing RenderFlex has an orientation of Axis.vertical.
// The edge of the RenderFlex that is overflowing has been marked in the rendering with a yellow and
// black striped pattern. This is usually caused by the contents being too big for the RenderFlex.
// Consider applying a flex factor (e.g. using an Expanded widget) to force the children of the
// RenderFlex to fit within the available space instead of being sized to their natural size.
// This is considered an error condition because it indicates that there is content that cannot be
// seen. If the content is legitimately bigger than the available space, consider clipping it with a
// ClipRect widget before putting it in the flex, or using a scrollable container rather than a Flex,
// like a ListView.
// The specific RenderFlex in question is: RenderFlex#f0cbc relayoutBoundary=up2 OVERFLOWING:
//   needs compositing
//   creator: Column ← Center ← KeyedSubtree-[GlobalKey#110e6] ← _BodyBuilder ← MediaQuery ←
//     LayoutId-[<_ScaffoldSlot.body>] ← CustomMultiChildLayout ← _ActionsScope ← Actions ←
//     AnimatedBuilder ← DefaultTextStyle ← AnimatedDefaultTextStyle ← ⋯
//   parentData: offset=Offset(0.0, 0.0) (can use size)
//   constraints: BoxConstraints(0.0<=w<=393.0, 0.0<=h<=737.0)
//   size: Size(393.0, 737.0)
//   direction: vertical
//   mainAxisAlignment: start
//   mainAxisSize: max
//   crossAxisAlignment: center
//   verticalDirection: down