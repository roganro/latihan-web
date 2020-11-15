<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\GaleriController;

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

Route::get('/jalan', function () {
    return view('arah');
});

Route::get('/galeri', [GaleriController::class, 'index']);
Route::get('/galeri/2', 'App\Http\Controllers\GaleriController@show');
Route::get('/artikel/{judul}', [GaleriController::class, 'dinamis']);
