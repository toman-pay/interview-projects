import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
final themeData = Theme.of(context);

    return Scaffold(
      appBar: AppBar(title: const Text('ساخت تراکنش')),
      floatingActionButton: FloatingActionButton.extended(onPressed: (){}, 
      label: const  Text('تایید',) ),
      body: Container(color: Colors.red),
    );
  }
}
