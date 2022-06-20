import 'package:dio/dio.dart';
import 'package:flutter_toman/common/exception.dart';

mixin HttpResponseValidation {
  validateResposnse(Response response) {
    if (response.statusCode != 204) {
      throw AppException(message: 'خطایی رخ داده است');
    }
  }
}