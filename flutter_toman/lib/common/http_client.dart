import 'package:dio/dio.dart';

final httpClient = Dio(BaseOptions(baseUrl: 'https://run.mocky.io/v3/'))
  ..interceptors.add(InterceptorsWrapper(
    onRequest: (options, handler) {
      {
        options.headers['Content-type'] = 'application/json';
        handler.next(options);
      }
    },
  ));
