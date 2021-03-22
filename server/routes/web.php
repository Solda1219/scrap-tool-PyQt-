<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});


Route::get('/register', [App\Http\Controllers\UserController::class, 'register'])->name('user.register');
Route::get('/login', [App\Http\Controllers\UserController::class, 'login'])->name('user.login');
Route::get('/logout', [App\Http\Controllers\UserController::class, 'logout'])->name('user.logout');
Route::get('/alertLoginStatus', [App\Http\Controllers\UserController::class, 'alertLoginStatus'])->name('user.alert');