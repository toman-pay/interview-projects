import 'package:flutter/material.dart';
import 'package:interview_projects/confg/design.dart';
import 'package:interview_projects/confg/theme.dart';

class TomanButton extends StatelessWidget {
  final String title;
  final VoidCallback onPressed;
  final bool enabled;
  const TomanButton({
    Key? key,
    required this.title,
    required this.onPressed,
    this.enabled = true,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: MaterialButton(
        height: 48,
        onPressed: enabled ? onPressed : null,
        color: Theme.of(context).colorScheme.primary,
        disabledColor: Colors.grey,
        shape: RoundedRectangleBorder(
          borderRadius: DesignConfig.highBorderRadius,
        ),
        child: Text(
          title,
          style: Theme.of(context)
              .textTheme
              .bodyText2!
              .copyWith(color: Colors.white),
        ),
      ),
    );
  }
}
