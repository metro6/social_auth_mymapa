$('form.register-form').validate({
    rules: {
      first_name: {
        required: true,
      },
      last_name: {
        required: true,
      },
      email: {
        email: true,
        required: true,
      },
      password: {
        required: true,
        minlength: 8,
        equalTo: '#password2'
      },
      password2: {
        required: true,
        minlength: 8,
      }

    },
    submitHandler: function (form) {
      var self = $(form);
      data = {'email': self.find('input[name="email"]').val(),
              'username': self.find('input[name="first_name"]').val(),
              'last_name': self.find('input[name="last_name"]').val(),
              'password': self.find('input[name="password"]').val(),
              };
      $.ajax({
        url: '/user/login',
        data: data,
        method: 'post',
        headers: {'X-CSRFToken': $.cookie('csrftoken')},
        dataType: 'json',
        success: function (response) {
          console.log(response);
          if (response.status == 'success') {
            self[0].reset();
            location = '/'
          };
          if (response.status == 'error') {
            $(form).find('p.errors').html(response['message'])
          };
        },
      });
    }
  })

$('button#show-login-form').on('click', function () {
  $('form.login-form').show();
  $('form.register-form').hide();
  $(this).hide();
})

$('form.login-form').validate({
    rules: {
      email: {
        required: true,
        email: true,
      },
      password: {
        required: true,
      },
    },
    submitHandler: function (form) {
      var self = $(form);
      data = {'email': self.find('input[name="email"]').val(),
              'password': self.find('input[name="password"]').val(),
              };
      $.ajax({
        url: '/user/login_view',
        data: data,
        method: 'post',
        headers: {'X-CSRFToken': $.cookie('csrftoken')},
        dataType: 'json',
        success: function (response) {
          console.log(response);
          if (response.status == 'success') {
            self[0].reset();
            location = '/'
          };
          if (response.status == 'error') {
            $(form).find('p.errors').html(response['message'])
          };
        },
      });
    }
  })