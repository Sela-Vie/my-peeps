<?php

namespace App\Http\Controllers;

use App\Models\Person;
use Illuminate\Http\Request;

class PersonController
{
    public function index()
    {
        return Person::all();
    }

    public function store(Request $request)
    {
        $data = $request->validate([
            'name_display' => 'required|string|max:255',
            'name_full' => 'required|string|max:255',
            'birth_date' => 'required|integer|min:1|max:31',
            'birth_month' => 'required|integer|min:1|max:12',
            'birth_year' => 'required|integer|min:1800|max:2100',
        ]);

        return Person::create($data);
    }

    public function show(Person $person)
    {
        return $person;
    }

    public function update(Request $request, Person $person)
    {
        $data = $request->validate([
            'name_display' => 'sometimes|string|max:255',
            'name_full' => 'sometimes|string|max:255',
            'birth_date' => 'sometimes|integer|min:1|max:31',
            'birth_month' => 'sometimes|integer|min:1|max:12',
            'birth_year' => 'sometimes|integer|min:1800|max:2100',
        ]);

        $person->update($data);

        return $person;
    }

    public function destroy(Person $person)
    {
        $person->delete();

        return response()->noContent();
    }
}
