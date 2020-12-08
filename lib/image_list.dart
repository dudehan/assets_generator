import 'package:flutter/material.dart';
import 'image_r.dart';

class ImageList extends StatefulWidget {
  @override
  _ImageListState createState() => _ImageListState();
}

class _ImageListState extends State<ImageList> {
  List<String> _images = [
    ImageR.imagesAeIcon,
    ImageR.imagesAnteIcon,
    ImageR.imagesArnIcon,
    ImageR.imagesBatIcon,
    ImageR.imagesBetIcon
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('ImageList')),
      body: ListView.separated(
        itemCount: _images.length,
        itemBuilder: (ctx, index) {
          return Container(
            height: 80,
            child: Image.asset(_images[index]),
          );
        },
        separatorBuilder: (ctx, index) {
          return Divider(color: Color.fromRGBO(122, 122, 122, 1), height: 1, indent: 15, endIndent: 15);
        },
      ),
    );
  }
}
