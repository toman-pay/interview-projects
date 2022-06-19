import 'package:flutter/material.dart';
import 'package:flutter_toman/theme.dart';
import 'package:flutter_toman/ui/home/home.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    const defaultTextStyle = TextStyle(
        fontFamily: 'IranYekan', color: LightThemeColors.primaryTextColor);
    return MaterialApp(
      title: 'Flutter',
      theme: ThemeData(
        hintColor: LightThemeColors.secondryTextColor,
        inputDecorationTheme: InputDecorationTheme(
            border: const OutlineInputBorder(),
            enabledBorder: OutlineInputBorder(
                borderSide: BorderSide(
                    color:
                        LightThemeColors.primaryTextColor.withOpacity(0.1)))),
        appBarTheme: AppBarTheme(
            titleTextStyle: defaultTextStyle.copyWith(fontSize: 14),
            backgroundColor: Colors.white,
            foregroundColor: LightThemeColors.primaryTextColor,
            elevation: 0),
        textTheme: TextTheme(
          button: defaultTextStyle.copyWith(
              color: LightThemeColors.primaryColor,
              fontWeight: FontWeight.bold,
              fontSize: 16),
          subtitle2: defaultTextStyle,
          bodyText2: defaultTextStyle,
          caption:
              defaultTextStyle.apply(color: LightThemeColors.secondryTextColor),
        ),
        colorScheme: const ColorScheme.light(
          primary: LightThemeColors.primaryColor,
          secondary: LightThemeColors.primaryColor,
          onSecondary: Colors.white,
          surfaceVariant: Colors.white,
        ),
        snackBarTheme: SnackBarThemeData(
            contentTextStyle: defaultTextStyle.apply(color: Colors.white)),
      ),
      home: const Directionality(
          textDirection: TextDirection.rtl, child: HomeScreen()),
    );
  }
}
