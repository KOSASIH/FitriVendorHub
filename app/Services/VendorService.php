<?php

namespace App\Services;

use App\Models\Vendor;
use App\Models\VendorVerification;
use App\Repositories\VendorRepository;

class VendorService
{
    private $vendorRepository;

    public function __construct(VendorRepository $vendorRepository)
    {
        $this->vendorRepository = $vendorRepository;
    }

    public function createVendor(array $data)
    {
        $vendor = $this->vendorRepository->createVendor($data);
        $this->createVerification($vendor, $data);
        return $vendor;
    }

    public function updateVendor(Vendor $vendor, array $data)
    {
        $this->vendorRepository->updateVendor($vendor, $data);
        $this->updateVerification($vendor, $data);
        return $vendor;
    }

    public function deleteVendor(Vendor $vendor)
    {
        $this->vendorRepository->deleteVendor($vendor);
    }

    public function verifyVendor(Vendor $vendor)
    {
        $vendor->verified = true;
        $vendor->save();
    }

    private function createVerification(Vendor $vendor, array $data)
    {
        $verification = new VendorVerification();
        $verification->vendor_id = $vendor->id;
        $verification->document_type = $data['document_type'];
        $verification->document_number = $data['document_number'];
        $verification->expiration_date = $data['expiration_date'];
        $verification->save();
    }

    private function updateVerification(Vendor $vendor, array $data)
    {
        $verification = $vendor->verification;
        $verification->document_type = $data['document_type'];
        $verification->document_number = $data['document_number'];
        $verification->expiration_date = $data['expiration_date'];
        $verification->save();
    }
}
