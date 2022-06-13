import 'package:flutter/cupertino.dart';

enum AppState { busy, idle, failed }

class CoreProvider with ChangeNotifier {
  AppState _appState = AppState.busy;

  set appState(AppState newState) {
    _appState = newState;
    notifyListeners();
  }

  AppState get appState => _appState;

  void update() => notifyListeners();
}
