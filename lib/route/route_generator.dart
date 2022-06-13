import 'package:flutter/material.dart';
import 'package:interview_projects/route/routes.dart';
import 'package:interview_projects/views/add_product/view.dart';
import 'package:interview_projects/views/add_product/state.dart';
import 'package:provider/provider.dart';

class RouteGenerator {
  static Route<dynamic> generateRoute(RouteSettings settings) {
    switch (settings.name) {
      case Routes.addProduct:
        return _createRoute(
          ChangeNotifierProvider<AddProductState>(
            create: (context) => AddProductState(),
            child: const AddProduct(),
          ),
        );
      default:
        return _errorRoute();
    }
  }

  static Route<dynamic> _errorRoute() {
    return MaterialPageRoute(builder: (_) {
      return Scaffold(
        appBar: AppBar(
          title: const Text('Error'),
        ),
        body: const Center(
          child: Text('ERROR'),
        ),
      );
    });
  }

  static Route _createRoute(page) {
    return MaterialPageRoute(
      builder: (context) => MediaQuery(
        data: MediaQuery.of(context).copyWith(textScaleFactor: 1.0),
        child: SafeArea(
          child: page,
          top: false,
        ),
      ),
    );
  }
}
