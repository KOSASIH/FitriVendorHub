<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class VendorVerification extends Model
{
    protected $fillable = [
        'vendor_id',
        'document_type',
        'document_number',
        'expiration_date',
    ];

    public function vendor()
    {
        return $this->belongsTo(Vendor::class);
    }
}
