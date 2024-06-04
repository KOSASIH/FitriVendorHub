<?php

namespace App\Repositories;

use App\Models\Vendor;

class VendorRepository
{
    public function getAllVendors()
    {
        return Vendor::all();
    }

    public function getVendorById($id)
    {
        return Vendor::find($id);
    }

    public function createVendor(array $data)
    {
        return Vendor::create($data);
    }

    public function updateVendor(Vendor $vendor, array $data)
    {
        $vendor->update($data);
        return $vendor;
    }

    public function deleteVendor(Vendor $vendor)
    {
        $vendor->delete();
    }
}
