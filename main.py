

<!DOCTYPE html>
<html>
<style>
form {
      background-color: lightgrey;
      padding: 20px;
      margin: 20px;
      width: 540px;
      font: 16px sans-serif;
      border-radius: 10px;
}
textarea {
         margin: 10px 0;
         width: 540px;
         height: 120px;
}
</style>
<body>

<form action="/action_page.php" method = "post" style="border:1px solid #ccc">
  <div>
    <label for = "rot">Rotate by:</label>
    <input name="rot" value = "0" placeholder = "0" type = "text">
    <p class = "Error"> </p>
  </div>  
   <p>
    <textarea type="text"  name="text" required></textarea>   
   </p>
  <div>   
    <input type="submit" value = "Submit query" />
  </div>
</form>

</body>
</html>
