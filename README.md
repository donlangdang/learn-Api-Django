### bộ code học django cơ bản của mình và sau này cũng sẽ dùng làm bộ code test các chức năng trong django và các thư viện liên quan tới nó

### bộ code này để học, và thử nghiệm 1 số thứ mình thích chứ không làm cho dự án thực tế

### link các thứ liên quan tới django

- model làm việc với database:

  - djangdo model meta option: https://docs.djangoproject.com/en/5.0/ref/models/options/

  - django field: https://docs.djangoproject.com/en/5.0/ref/models/fields/

- truy vấn vào database sau khi đã tạo được model và lưu vào datasebase (model ở đây được hiểu là bảng trong sql)
  - truy vấn model.objects....: https://docs.djangoproject.com/en/5.0/topics/db/queries/

### link các thứ liên qua tới rest_framework

- serializers chuyển đổi dữ liệu từ object sang các dạng khác:

  - serializers: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

  - quan hệ giữa các model: https://www.django-rest-framework.org/api-guide/relations/

### những thứ liên quan tới view:

- view để tương tác với internet qua các phương thức GET POST DELETE UPDATE PUT:

  - view: https://www.django-rest-framework.org/api-guide/views/

### thông tin và các thư viện, framework dùng trong dự án để sử dụng cho semantic versioning cho những thứ sau này

```
* asgiref==3.8.1
*  Django==5.0.6
* django-environ==0.11.2
* djangorestframework==3.15.1
* mysqlclient==2.2.4
* sqlparse==0.5.0
```

### học thêm tại: https://github.com/duonghuuthanh/K19-RestfulApiDemo
