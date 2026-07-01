<?php

namespace App\Models;

use Database\Factories\PersonFactory;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\SoftDeletes;

#[Fillable([
    'name_display',
    'name_full',
    'birth_date',
    'birth_month',
    'birth_year',
])]
class Person extends Model
{
    /** @use HasFactory<PersonFactory> */
    use HasFactory, SoftDeletes;

    protected function casts(): array
    {
        return [
            'birth_date' => 'integer',
            'birth_month' => 'integer',
            'birth_year' => 'integer',
        ];
    }

    public function personDataEntries(): HasMany
    {
        return $this->hasMany(PersonDataEntry::class);
    }
}
