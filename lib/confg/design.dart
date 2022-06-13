import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class DesignConfig {
  static final lowBorderRadius = BorderRadius.circular(8);
  static final mediumBorderRadius = BorderRadius.circular(12);
  static final highBorderRadius = BorderRadius.circular(24);

  static SystemUiOverlayStyle get systemUiOverlayStyle =>
      const SystemUiOverlayStyle(
        statusBarIconBrightness: Brightness.dark,
        statusBarColor: Colors.white,
        systemNavigationBarColor: Colors.white,
        systemNavigationBarDividerColor: Colors.transparent,
        systemNavigationBarIconBrightness: Brightness.dark,
      );
}
