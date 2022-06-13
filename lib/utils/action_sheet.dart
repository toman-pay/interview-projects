import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:interview_projects/confg/theme.dart';
import 'package:interview_projects/views/widgets/button.dart';

class ActionSheetUtils {
  static void showLoadingIndicator(context) {
    showDialog(
      barrierDismissible: false,
      context: context,
      builder: (context) => Center(
        child: SpinKitSquareCircle(
          color: Theme.of(context).colorScheme.primary,
        ),
      ),
    );
  }

  static Future<void> showBottomSheet({
    required String title,
    required String description,
    required String buttonTitle,
    required BuildContext context,
    required VoidCallback onPressed,
  }) async {
    await showModalBottomSheet(
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      context: context,
      builder: (context) => Container(
        padding: const EdgeInsets.all(24).copyWith(top: 0),
        decoration: BoxDecoration(
          color: Theme.of(context).colorScheme.surface,
          borderRadius: const BorderRadius.vertical(
            top: Radius.circular(16),
          ),
        ),
        child: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(height: 20),
              Center(
                child: Container(
                  height: 3,
                  width: 50,
                  color: Theme.of(context).colorScheme.grey,
                ),
              ),
              const SizedBox(height: 12),
              Text(title),
              const SizedBox(height: 16),
              Text(
                description,
                style: Theme.of(context).textTheme.caption,
              ),
              const SizedBox(height: 28),
              TomanButton(
                title: buttonTitle,
                onPressed: onPressed,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
