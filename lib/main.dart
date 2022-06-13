import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:interview_projects/confg/design.dart';
import 'package:interview_projects/confg/theme.dart';
import 'package:interview_projects/route/route_generator.dart';
import 'package:interview_projects/route/routes.dart';

void main() {
  SystemChrome.setSystemUIOverlayStyle(DesignConfig.systemUiOverlayStyle);
  runApp(const TomanTest());
}

class TomanTest extends StatelessWidget {
  const TomanTest({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Toman Test',
      debugShowCheckedModeBanner: false,
      theme: ThemeConfing.data,
      initialRoute: Routes.addProduct,
      onGenerateRoute: RouteGenerator.generateRoute,
      localizationsDelegates: const [
        GlobalCupertinoLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale("fa", "IR"),
      ],
      locale: const Locale("fa", "IR"),
    );
  }
}
