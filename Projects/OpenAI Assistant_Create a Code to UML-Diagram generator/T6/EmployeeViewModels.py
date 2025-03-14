using FuelStation.Model;
using System.ComponentModel.DataAnnotations;

namespace FuelStation.Blazor.Shared.ViewModels
{
    public class VerifiedEmployeeViewModel
    {
        public Guid ID { get; set; }
        public string FullName { get; set; }
        public string Username { get; set; }
        public EmployeeTypeEnum EmployeeType { get; set; }
    }

    public class EmployeeListViewModel
    {
        public Guid ID { get; set; }
        public string FullName { get; set; }
        public string Username { get; set; }
        public EmployeeTypeEnum EmployeeType { get; set; }
        public DateTime HireDateStart { get; set; }
        public DateTime? HireDateEnd { get; set; }
        public decimal SallaryPerMonth { get; set; }
    }

    public class EmployeeViewModel
    {
        public Guid ID { get; set; }
        [Required]
        [MaxLength(20, ErrorMessage = "Name has max length 20 characters.")]
        public string Name { get; set; }
        [Required]
        [MaxLength(20, ErrorMessage = "Surname has max length 20 characters.")]
        public string Surname { get; set; }
        [Required]
        public EmployeeTypeEnum EmployeeType { get; set; }
        [Required]
        public DateTime HireDateStart { get; set; }
        public DateTime? HireDateEnd { get; set; }
        [Required]
        [Range(0, 99999.99, ErrorMessage = "Invalid Salary [0-99999.99]")]
        public decimal SallaryPerMonth { get; set; }
        [Required]
        [MaxLength(20, ErrorMessage = "Username has max length 20 characters.")]
        public string Username { get; set; }
        [Required]
        [MaxLength(256, ErrorMessage = "Password has max length 256 characters.")]
        public string Password { get; set; }

    }
}