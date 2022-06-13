import 'dart:convert';
import 'dart:developer';
import 'package:http/http.dart' as http;

class RequestService {
  static late String token;
  int? statusCode;

  String errorMessage =
      'خطا! لطفا اتصال اینترنت خود را بررسی و مجددا تلاش نمایید.';

  Map<String, dynamic> get result => _body ?? {};

  Map<String, dynamic>? _body;
  final Map<String, String> _headers = {
    "accept": "*/*",
    "Content-Type": "application/json; charset=UTF-8",
  };
  final String url;
  Map? _requestBody;

  bool isSuccess = false;

  RequestService(
    this.url, {
    Map<String, String>? requestHeaders,
    body,
  }) {
    if (body != null) _requestBody = body;
    if (requestHeaders != null) _headers.addAll(requestHeaders);
    if (body != null) _requestBody = body;
  }

  String? get _generateBody =>
      _requestBody == null ? null : jsonEncode(_requestBody);

  Future<void> post() async {
    try {
      final response = await http
          .post(
            Uri.parse(url),
            body: _generateBody,
            headers: _headers,
          )
          .timeout(
            const Duration(seconds: 10),
          )
          .catchError(
        (e) {
          throw e;
        },
      );
      _handleResponse(response);
    } catch (e) {
      _handleError(null);
    }
  }

  void _handleResponse(http.Response? response) {
    statusCode = response?.statusCode;
    if (_handleError(response)) {
      if (response!.body.isNotEmpty) {
        _body = Map<String, dynamic>.from(json.decode(response.body));
      }
    }
  }

  bool _handleError(http.Response? response) {
    if (response == null) {
      log(
        'Connecion failed or request timedout! ("$url")',
        name: 'Request fail error',
      );
      isSuccess = false;
      return false;
    }
    if (response.statusCode != 200 && response.statusCode != 204) {
      dynamic data;
      if (response.body.isEmpty) {
        data = 'No results!';
      } else if (response.body.contains('<!DOCTYPE html>')) {
        data = response.body;
      } else {
        data = jsonDecode(response.body);
      }
      log(
        'Request to [$url] failed with status code ${response.statusCode} & result : \n $data',
        name: 'Request fail error',
      );
      isSuccess = false;
      return false;
    }
    isSuccess = true;
    return true;
  }
}
