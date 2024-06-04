use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    public function products()
    {
        return $this->belongsToMany(Product::class);
    }
}
