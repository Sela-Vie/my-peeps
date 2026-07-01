<?php

namespace App\Http\Controllers;

use App\Models\Person;
use App\Models\PersonDataEntry;
use Illuminate\Http\Request;

class PersonDataEntryController
{
    public function index(Person $person)
    {
        return $person->personDataEntries;
    }

    public function store(Request $request, Person $person)
    {
        $data = $request->validate([
            'data_entry_content' => 'required|string|max:1000',
        ]);

        return $person->personDataEntries()->create($data);
    }

    public function show(Person $person, PersonDataEntry $personDataEntry)
    {
        return $personDataEntry;
    }

    public function update(Request $request, Person $person, PersonDataEntry $personDataEntry)
    {
        $data = $request->validate([
            'data_entry_content' => 'sometimes|string|max:1000',
        ]);

        $personDataEntry->update($data);

        return $personDataEntry;
    }

    public function destroy(Person $person, PersonDataEntry $personDataEntry)
    {
        $personDataEntry->delete();

        return response()->noContent();
    }
}
