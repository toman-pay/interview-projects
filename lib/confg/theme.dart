import 'package:flutter/material.dart';

class ThemeConfing {
  static final data = ThemeData(
    primarySwatch: Colors.amber,
    fontFamily: 'iransans',
    colorScheme: const ColorScheme(
      brightness: Brightness.light,
      primary: Color(0XFF00897B),
      onPrimary: Colors.white,
      secondary: Colors.white,
      onSecondary: Colors.black,
      error: Colors.red,
      onError: Colors.white,
      background: Colors.white,
      onBackground: Color(0XFF00897B),
      surface: Colors.white,
      onSurface: Colors.white,
    ),
    checkboxTheme: CheckboxThemeData(
      fillColor: MaterialStateProperty.all<Color>(const Color(0XFF00897B)),
    ),
    textTheme: const TextTheme(
      bodyText2: TextStyle(fontWeight: FontWeight.bold),
    ),
  );
}

extension TomanColorScheme on ColorScheme {
  Color get grey => const Color(0XFF6A90A2);
}
