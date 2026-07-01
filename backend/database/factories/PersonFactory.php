<?php

namespace Database\Factories;

use App\Models\Person;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends Factory<Person>
 */
class PersonFactory extends Factory
{
    protected $model = Person::class;

    public function definition(): array
    {
        return [
            'name_display' => 'fake_' . fake()->firstName(),
            'name_full' => 'fake_' . fake()->name(),
            'birth_date' => fake()->numberBetween(1, 28),
            'birth_month' => fake()->numberBetween(1, 12),
            'birth_year' => fake()->numberBetween(1950, 2025),
        ];
    }
}
