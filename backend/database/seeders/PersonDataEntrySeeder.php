<?php

namespace Database\Seeders;

use App\Models\Person;
use App\Models\PersonDataEntry;
use Illuminate\Database\Seeder;

class PersonDataEntrySeeder extends Seeder
{
    public function run(): void
    {
        $people = Person::all();

        if ($people->isEmpty()) {
            Person::factory(10)->create();
            $people = Person::all();
        }

        $people->each(function (Person $person) {
            PersonDataEntry::factory(fake()->numberBetween(1, 5))->create([
                'person_id' => $person->id,
            ]);
        });
    }
}
