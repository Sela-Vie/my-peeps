<?php

namespace App\Models;

use Database\Factories\PersonDataEntryFactory;
use Illuminate\Database\Eloquent\Attributes\Fillable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\SoftDeletes;

#[Fillable([
    'person_id',
    'data_entry_content',
])]
class PersonDataEntry extends Model
{
    /** @use HasFactory<PersonDataEntryFactory> */
    use HasFactory, SoftDeletes;

    public function person(): BelongsTo
    {
        return $this->belongsTo(Person::class);
    }
}
