<?php

namespace Database\Factories;

use App\Models\Person;
use App\Models\PersonDataEntry;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends Factory<PersonDataEntry>
 */
class PersonDataEntryFactory extends Factory
{
    protected $model = PersonDataEntry::class;

    public function definition(): array
    {
        return [
            'person_id' => Person::factory(),
            'data_entry_content' => fake()->text(200),
        ];
    }
}
