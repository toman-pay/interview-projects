import 'package:flutter/cupertino.dart';
import 'package:intl/intl.dart';

const defaultScrollPhsics = BouncingScrollPhysics();

extension PriceLabel on String {
  String get numberFormat =>
      NumberFormat.decimalPattern().format(int.parse(this));
}
