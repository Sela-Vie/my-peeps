<?php

use App\Http\Controllers\PersonController;
use App\Http\Controllers\PersonDataEntryController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get('/health', function () {
    return response()->json(['status' => 'ok']);
});

Route::apiResource('people', PersonController::class);
Route::apiResource('people.person-data-entries', PersonDataEntryController::class);
