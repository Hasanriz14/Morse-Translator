$(document).ready(function () {
  $("#form-get-string").on("submit", function (event) {
    event.preventDefault();

    $.ajax({
      url: "/submit",
      type: "POST",
      data: $(this).serialize(),
      success: function (response) {
        $("#translate-text").html(response);
        $("#get-string").val("");
      },
    });
  });
});
