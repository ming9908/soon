import 'package:flutter/material.dart';
import 'package:table_calendar/table_calendar.dart';

Widget weekCalendar () {
  return (
    TableCalendar(
      startingDayOfWeek: setStarting(DateTime.now().subtract(const Duration(days: 3))), /** 시작요일 */
      calendarFormat: CalendarFormat.week,  /** 달력 표기 형식(월/2주/1주) */
      firstDay: DateTime.now().subtract(const Duration(days: 3)), /** 달력 시작 날짜 */
      lastDay: DateTime.now().add(const Duration(days: 3,)),  /** 달력 종료 날짜 */
      focusedDay: DateTime.now().add(const Duration(days: 2,)), /** 색칠데이 */
      headerVisible: false, /** 달력 상단부 */
    )
  );
}

StartingDayOfWeek setStarting (DateTime date) {
  return switch (date.weekday) {
    1 => StartingDayOfWeek.monday,
    2 => StartingDayOfWeek.tuesday,
    3 => StartingDayOfWeek.wednesday,
    4 => StartingDayOfWeek.thursday,
    5 => StartingDayOfWeek.friday,
    6 => StartingDayOfWeek.saturday,
    _ => StartingDayOfWeek.sunday
  };
}