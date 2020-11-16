<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class GaleriController extends Controller
{
    public function index()
    {
        return view('arah');
    }
    
    public function show()
    {
        return view('arah');
    }
    
    public function dinamis($slug)
    {
        die($slug);
    }
}
