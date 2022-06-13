import 'package:interview_projects/providers/core.dart';
import 'package:interview_projects/services/network/request.dart';
import 'package:interview_projects/services/network/requst_helper.dart';

class AddProductState extends CoreProvider {
  String title = '';
  String price = '';
  String description = '';
  bool _termsAccepted = false;

  bool get termsAccepted => _termsAccepted;
  set termsAccepted(bool value) {
    _termsAccepted = value;
    notifyListeners();
  }

  Future<bool> addProduct() async {
    final service = RequestService(
      RequestHelper.addProduct,
      body: {
        'title': title,
        'description': description,
        'price': price,
      },
    );
    await service.post();
    return service.isSuccess;
  }
}
