import 'package:flutter/material.dart';
import 'package:interview_projects/confg/design.dart';

class TomanButton extends StatelessWidget {
  final String title;
  final VoidCallback onPressed;
  const TomanButton({
    Key? key,
    required this.title,
    required this.onPressed,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: MaterialButton(
        height: 48,
        onPressed: onPressed,
        color: Theme.of(context).colorScheme.primary,
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
