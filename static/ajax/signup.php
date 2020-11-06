<?php
$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$email = $_POST['email'];
$password = $_POST['password'];

echo json_encode( array(
                            'status' => 'success',
                            'message' => sprintf( 'signup successful. You entered<br />First Name: %1$s<br />Last Name: %2$s<br />Email: %3$s<br />Password: %4$s',
                                                   $firstname,
                                                   $lastname,
                                                   $email,
                                                   $password
                                                ),
                       )
                );
?>